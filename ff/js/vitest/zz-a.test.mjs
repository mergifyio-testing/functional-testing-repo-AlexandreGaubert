import { expect, test } from "vitest";
import { broken } from "../flags.mjs";

test("test A", () => {
  expect(broken("a"), "A broken by these runs").toEqual([]);
});
