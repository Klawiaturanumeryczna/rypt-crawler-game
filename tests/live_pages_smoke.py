import os
from playwright.sync_api import expect, sync_playwright

URL = os.environ.get(
    "CRYPT_CRAWLER_LIVE_URL",
    "https://klawiaturanumeryczna.github.io/rypt-crawler-game/",
)


def main():
    page_errors = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.on("pageerror", lambda error: page_errors.append(str(error)))

        response = page.goto(URL, wait_until="domcontentloaded", timeout=60_000)
        assert response is not None, f"No HTTP response from published game: {URL}"
        assert response.status == 200, f"Published game returned HTTP {response.status}: {URL}"

        expect(page).to_have_title("Crypt Crawler — prototyp")
        canvas = page.locator("#game")
        expect(canvas).to_be_visible()
        expect(page.locator("#overlayTitle")).to_have_text("CRYPT CRAWLER")
        expect(page.locator("#startBtn")).to_have_text("ROZPOCZNIJ RUN")

        # Exercise the real published startup flow: title -> weapon -> movement -> gameplay.
        page.locator("#startBtn").click()
        expect(page.locator("#overlayTitle")).to_have_text("WYBIERZ STYL STRZELANIA")
        page.locator("button.fire-precision").click()
        expect(page.locator("#overlayTitle")).to_have_text("WYBIERZ STYL RUCHU")
        page.locator("button.move-drifter").click()
        expect(page.locator("#overlay")).to_be_hidden()
        expect(page.locator("#floor")).to_have_text("1")
        expect(page.locator("#room")).to_have_text("1")
        page.wait_for_timeout(500)

        assert not page_errors, "JavaScript errors on published page: " + " | ".join(page_errors)
        print(f"Published game smoke passed: {URL}")
        browser.close()


if __name__ == "__main__":
    main()
