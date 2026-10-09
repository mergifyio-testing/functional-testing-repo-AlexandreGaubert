require "spec_helper"

RSpec.describe "target" do
  it("test A") { expect(FfFlags.broken("a")).to eq([]) }
end
