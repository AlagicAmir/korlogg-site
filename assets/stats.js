/* korlogg.com – App Store / Google Play badge clicks to TelemetryDeck. No cookies, no storage:
   one random id per page load, hashed, never kept. Page views are sent by
   TelemetryDeck's Web SDK. Fire and forget; navigation is never delayed. */
(function () {
  "use strict";
  var APP_ID = "22120ED7-73AC-47F1-8E16-CAF4203EE530";
  var ENDPOINT = "https://nom.telemetrydeck.com/v2/";
  var test = /^(localhost|127(\.\d+){3}|\[::1\])$/.test(location.hostname);
  var lang = document.documentElement.lang || "";
  var session = Math.random().toString(36).slice(2) + Date.now().toString(36);
  var user = null;
  try {
    crypto.subtle.digest("SHA-256", new TextEncoder().encode(session)).then(function (buf) {
      user = Array.prototype.map.call(new Uint8Array(buf), function (b) { return ("0" + b.toString(16)).slice(-2); }).join("");
    });
  } catch (e) {}

  function send(type, payload) {
    if (!user) return;
    var body = { appID: APP_ID, clientUser: user, sessionID: session, type: type,
                 telemetryClientVersion: "korlogg.com stats.js 1", payload: payload };
    if (test) body.isTestMode = true;
    try {
      fetch(ENDPOINT, { method: "POST", mode: "cors", keepalive: true,
                        headers: { "Content-Type": "application/json" }, body: JSON.stringify([body]) })
        .catch(function () {});
    } catch (e) {}
  }

  // Android visitors: links with data-play (the header "Get the app") go to Google Play.
  if (/Android/i.test(navigator.userAgent)) {
    var swap = function () {
      Array.prototype.forEach.call(document.querySelectorAll("a[data-play]"), function (a) {
        a.href = a.getAttribute("data-play");
        a.setAttribute("data-position", a.getAttribute("data-position") + "_play");
      });
    };
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", swap); else swap();
  }

  document.addEventListener("click", function (e) {
    var a = e.target && e.target.closest ? e.target.closest("a.store-badge, a[data-position]") : null;
    if (!a) return;
    send("AppStoreBadge.clicked", { language: lang, path: location.pathname, position: a.getAttribute("data-position") || "other" });
  }, true);
})();
