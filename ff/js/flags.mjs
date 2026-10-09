// Flag files the failure-first e2e pull requests add to break or fix a test;
// same rule as ff/flags.py.
import { existsSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const FLAGS = join(dirname(fileURLToPath(import.meta.url)), "..", "flags");

export function broken(test) {
  return readdirSync(FLAGS)
    .filter((f) => f.endsWith(`.break_${test}`))
    .map((f) => f.split(".")[0])
    .filter((run) => !existsSync(join(FLAGS, `${run}.fix_${test}`)))
    .sort();
}
