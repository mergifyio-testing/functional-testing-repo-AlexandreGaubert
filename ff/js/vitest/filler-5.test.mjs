import { test } from "vitest";

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

for (let n = 1; n <= 3; n++) {
  test(`filler 5.${n}`, async () => {
    await sleep(3000);
  }, 10000);
}
