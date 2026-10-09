import { test } from "@mergifyio/playwright";

for (let n = 1; n <= 3; n++) {
  test(`filler 1.${n}`, async () => {
    await new Promise((r) => setTimeout(r, 3000));
  });
}
