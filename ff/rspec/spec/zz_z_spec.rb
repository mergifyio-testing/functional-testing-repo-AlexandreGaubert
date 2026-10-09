require "spec_helper"

RSpec.describe "target" do
  it("test Z") { expect(FfFlags.broken("z")).to eq([]) }
end
