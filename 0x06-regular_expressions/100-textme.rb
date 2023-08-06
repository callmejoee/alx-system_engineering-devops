#!/usr/bin/env ruby
puts ARGV[0].scan(/(\bfrom:\K\S+(?=\])|\bto:\+\K?(\w+)|\bflags:\K\S+(?=\]))/).join
