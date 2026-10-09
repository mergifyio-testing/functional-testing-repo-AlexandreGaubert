import MergifyReporter from "@mergifyio/vitest";
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["vitest/**/*.test.mjs"],
    maxWorkers: 2,
    reporters: ["verbose", new MergifyReporter()],
  },
});
