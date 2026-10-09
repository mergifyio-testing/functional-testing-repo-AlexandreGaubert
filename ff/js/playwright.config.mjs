import { defineConfig } from "@playwright/test";
import { withMergify } from "@mergifyio/playwright";

export default withMergify(
  defineConfig({
    testDir: "playwright",
    workers: 2,
    reporter: [["list"]],
  }),
);
