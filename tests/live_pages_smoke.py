import os
import time
from playwright.sync_api import Error as PlaywrightError, expect, sync_playwright

URL = os.environ.get(
    "CRYPT_CRAWLER_LIVE_URL",
    "https://klawiaturanumeryczna.github.io/rypt-crawler-game/",
)
DEPLOYED_HELP_MARKER = "przeciwnicy w promieniu 420 px"


def main():
    page_errors = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            page.on("pageerror", lambda error: page_errors.append(str(error)))

            # Pages deploys asynchronously after a push. Retry until the live URL
            # serves this build's unique help text, not a cached previous version.
            deadline = time.monotonic() + 180
            response = None
            last_issue = "No response attempted yet"
            while time.monotonic() < deadline:
                try:
                    response = page.goto(URL, wait_until="domcontentloaded", timeout=30_000)
                    if response is None:
                        last_issue = "No HTTP response"
                    elif response.status != 200:
                        last_issue = f"HTTP {response.status}"
                    elif DEPLOYED_HELP_MARKER not in page.locator(".controls").inner_text():
                        last_issue = "HTTP 200, but Pages still serves the previous floor-help text"
                    else:
                        break
                except PlaywrightError as error:
                    last_issue = str(error)
                time.sleep(5)
            else:
                raise AssertionError(
                    f"Published build did not become current within 180 seconds: {last_issue}"
                )

            assert response is not None and response.status == 200, (
                f"Published game did not return HTTP 200: {URL}"
            )
            expect(page).to_have_title("Crypt Crawler — prototyp")
            expect(page.locator("#game")).to_be_visible()
            expect(page.locator("#overlayTitle")).to_have_text("CRYPT CRAWLER")
            expect(page.locator("#startBtn")).to_have_text("ROZPOCZNIJ RUN")

            # Exercise the real published startup flow: title -> weapon -> movement -> gameplay.
            page.locator("#startBtn").click()
            expect(page.locator("#overlayTitle")).to_have_text("WYBIERZ STYL STRZELANIA")
            page.locator("button.fire-scatter").click()
            expect(page.locator("#overlayTitle")).to_have_text("WYBIERZ STYL RUCHU")
            expect(page.locator("#moveChoices .moveChoice")).to_have_count(3)
            page.locator("button.move-drifter").click()
            expect(page.locator("#overlay")).to_be_hidden()
            expect(page.locator("#floor")).to_have_text("1")
            expect(page.locator("#room")).to_have_text("1")
            page.wait_for_timeout(500)

            assert not page_errors, "JavaScript errors on published page: " + " | ".join(page_errors)
            print(f"Published game smoke passed: {URL}")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
