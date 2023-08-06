#!/usr/bin/env ruby
puts ARGV[0].scan(/(\bfrom:\K\w+|\bto:\+\K\w+|\bflags:\K\S+(?=\]))/).join
