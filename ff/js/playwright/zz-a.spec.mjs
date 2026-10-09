import { expect, test } from "@mergifyio/playwright";
import { broken } from "../flags.mjs";

test("test A", () => {
  expect(broken("a"), "A broken by these runs").toEqual([]);
});
