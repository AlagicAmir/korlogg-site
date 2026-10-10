#!/usr/bin/env python3
"""Full-page screenshots of the sv/de/en home pages at phone and desktop width,
light and dark, via headless Chrome's DevTools protocol -> docs/screens/.
Needs the site served on 127.0.0.1:8766 (python3 -m http.server 8766 --bind 127.0.0.1)."""
import asyncio, base64, json, pathlib, subprocess, time, urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PAGES = {"en": "/", "sv": "/se/", "de": "/de/"}
SIZES = {"phone": (390, 844, 3, True), "desktop": (1440, 900, 1, False)}

async def shoot(ws_url):
    async with websockets.connect(ws_url, max_size=200_000_000) as ws:
        n = 0
        async def call(method, **params):
            nonlocal n; n += 1; my = n
            await ws.send(json.dumps({"id": my, "method": method, "params": params}))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("id") == my: return msg.get("result", {})
        for lang, path in PAGES.items():
            for name, (w, h, dpr, mobile) in SIZES.items():
                for scheme in ("light", "dark"):
                    await call("Emulation.setDeviceMetricsOverride", width=w, height=h, deviceScaleFactor=dpr, mobile=mobile)
                    await call("Emulation.setEmulatedMedia", features=[{"name": "prefers-color-scheme", "value": scheme}])
                    await call("Page.navigate", url=f"http://127.0.0.1:8766{path}")
                    await asyncio.sleep(1.5)
                    # load lazy images: scroll through the page
                    await call("Runtime.evaluate", expression="(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}scrollTo(0,0)})()", awaitPromise=True)
                    await asyncio.sleep(0.8)
                    m = await call("Page.getLayoutMetrics")
                    full_h = int(m["cssContentSize"]["height"]); full_w = int(m["cssContentSize"]["width"])
                    if full_w > w: print(f"WARNING {lang} {name}: page is {full_w}px wide at {w}px (horizontal scroll)")
                    # grow the viewport to the whole page so every lazy image loads and nothing tiles
                    await call("Emulation.setDeviceMetricsOverride", width=w, height=full_h, deviceScaleFactor=1, mobile=mobile)
                    await asyncio.sleep(2.0)
                    shot = await call("Page.captureScreenshot", format="png")
                    out = ROOT / f"docs/screens/{lang}-{name}-{scheme}.png"
                    out.write_bytes(base64.b64decode(shot["data"]))
                    print(out.name, w, full_h)

def main():
    proc = subprocess.Popen([CHROME, "--headless=new", "--remote-debugging-port=9333", "--hide-scrollbars",
                             "--user-data-dir=/tmp/korlogg-screens-profile", "about:blank"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(50):
            try:
                tabs = json.load(urllib.request.urlopen("http://127.0.0.1:9333/json")); break
            except Exception: time.sleep(0.2)
        page = [t for t in tabs if t["type"] == "page"][0]
        asyncio.run(shoot(page["webSocketDebuggerUrl"]))
    finally:
        proc.terminate()

if __name__ == "__main__":
    main()
