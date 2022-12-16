const puppeteer = require('puppeteer');
const path = require('path');

async function generateDocs() {
  const browser = await puppeteer.launch({
      headless: true,
      timeout: 100000
  });
  const page = await browser.newPage();
  const urls = ['https://gobyexample.com/hello-world', 'https://gobyexample.com/values', 'https://gobyexample.com/variables', 'https://gobyexample.com/constants', 'https://gobyexample.com/for', 'https://gobyexample.com/if-else', 'https://gobyexample.com/switch', 'https://gobyexample.com/arrays', 'https://gobyexample.com/slices', 'https://gobyexample.com/maps', 'https://gobyexample.com/range', 'https://gobyexample.com/functions', 'https://gobyexample.com/multiple-return-values', 'https://gobyexample.com/variadic-functions', 'https://gobyexample.com/closures', 'https://gobyexample.com/recursion', 'https://gobyexample.com/pointers', 'https://gobyexample.com/strings-and-runes', 'https://gobyexample.com/structs', 'https://gobyexample.com/methods', 'https://gobyexample.com/interfaces', 'https://gobyexample.com/struct-embedding', 'https://gobyexample.com/generics', 'https://gobyexample.com/errors', 'https://gobyexample.com/goroutines', 'https://gobyexample.com/channels', 'https://gobyexample.com/channel-buffering', 'https://gobyexample.com/channel-synchronization', 'https://gobyexample.com/channel-directions', 'https://gobyexample.com/select', 'https://gobyexample.com/timeouts', 'https://gobyexample.com/non-blocking-channel-operations', 'https://gobyexample.com/closing-channels', 'https://gobyexample.com/range-over-channels', 'https://gobyexample.com/timers', 'https://gobyexample.com/tickers', 'https://gobyexample.com/worker-pools', 'https://gobyexample.com/waitgroups', 'https://gobyexample.com/rate-limiting', 'https://gobyexample.com/atomic-counters', 'https://gobyexample.com/mutexes', 'https://gobyexample.com/stateful-goroutines', 'https://gobyexample.com/sorting', 'https://gobyexample.com/sorting-by-functions', 'https://gobyexample.com/panic', 'https://gobyexample.com/defer', 'https://gobyexample.com/recover', 'https://gobyexample.com/string-functions', 'https://gobyexample.com/string-formatting', 'https://gobyexample.com/text-templates', 'https://gobyexample.com/regular-expressions', 'https://gobyexample.com/json', 'https://gobyexample.com/xml', 'https://gobyexample.com/time', 'https://gobyexample.com/epoch', 'https://gobyexample.com/time-formatting-parsing', 'https://gobyexample.com/random-numbers', 'https://gobyexample.com/number-parsing', 'https://gobyexample.com/url-parsing', 'https://gobyexample.com/sha256-hashes', 'https://gobyexample.com/base64-encoding', 'https://gobyexample.com/reading-files', 'https://gobyexample.com/writing-files', 'https://gobyexample.com/line-filters', 'https://gobyexample.com/file-paths', 'https://gobyexample.com/directories', 'https://gobyexample.com/temporary-files-and-directories', 'https://gobyexample.com/embed-directive', 'https://gobyexample.com/testing-and-benchmarking', 'https://gobyexample.com/command-line-arguments', 'https://gobyexample.com/command-line-flags', 'https://gobyexample.com/command-line-subcommands', 'https://gobyexample.com/environment-variables', 'https://gobyexample.com/http-client', 'https://gobyexample.com/http-server', 'https://gobyexample.com/context', 'https://gobyexample.com/spawning-processes', 'https://gobyexample.com/execing-processes', 'https://gobyexample.com/signals', 'https://gobyexample.com/exit'];
  for (let url of urls) {
    await page.goto(url, { waitUntil: 'networkidle2' });
    const imageName = `${url.split('/').pop()}.png`;
    const imagePath = path.join('gobyexample', imageName);
    await page.screenshot({ path: imagePath, fullPage: true });
  }
  browser.close();
}

generateDocs();