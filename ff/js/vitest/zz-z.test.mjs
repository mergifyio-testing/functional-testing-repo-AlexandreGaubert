import { expect, test } from "vitest";
import { broken } from "../flags.mjs";

test("test Z", () => {
  expect(broken("z"), "Z broken by these runs").toEqual([]);
});
