require "spec_helper"

RSpec.describe "filler 5" do
  3.times do |n|
    it("waits #{n + 1}") { sleep 3 }
  end
end
