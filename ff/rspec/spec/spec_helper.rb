require "rspec_mergify"

module FfFlags
  DIR = File.expand_path("../../flags", __dir__)

  # Same rule as ff/flags.py.
  def self.broken(test)
    Dir.glob(File.join(DIR, "*.break_#{test}")).map { |f| File.basename(f).split(".").first }
       .reject { |run| File.exist?(File.join(DIR, "#{run}.fix_#{test}")) }.sort
  end
end
