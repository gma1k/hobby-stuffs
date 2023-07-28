#!/usr/bin/env ruby

def random_word(words)
  words.sample
end

adjectives = ["amazing", "awesome", "brilliant", "creative", "dazzling", "excellent", "fantastic", "gorgeous", "incredible", "joyful", "kind", "lovely", "marvelous", "nice", "outstanding", "perfect", "remarkable", "superb", "terrific", "wonderful"]

nouns = ["adventure", "beauty", "challenge", "dream", "experience", "friendship", "goal", "happiness", "imagination", "journey", "knowledge", "love", "magic", "nature", "opportunity", "passion", "quality", "reality", "success", "wisdom"]

motto = "Life is a #{random_word(adjectives)} #{random_word(nouns)}."

puts motto
