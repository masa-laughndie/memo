require "nkf"

voice = "キカイ"
hiragana = NKF.nkf("--hiragana -w", voice) # きかい
generic_words = [voice, hiragana]

# same_voice_tansi_lists = {
#   "きかい" => ["きかい", "機かい", "機会", "機械"],
#   "機かい" => ["きかい", "機かい", "機会", "機械"],
#   "機械"   => ["きかい", "機かい", "機械"],
#   "機械"   => ["きかい", "機械"],
#   "機会"   => ["きかい", "機かい", "機会", "き会", "キ会"],
#   "き会"   => ["きかい", "機会", "き会", "キ会"],
#   "キ会"   => ["きかい", "機会", "き会", "キ会"]
# }

same_voice_tansi_lists = [
  {key: "きかい", synonyms:  ["きかい", "機かい", "機会", "機械"]},
  {key: "機かい", synonyms:  ["きかい", "機かい", "機会", "機械"]},
  {key: "機械", synonyms:  ["きかい", "機かい", "機械"]},
  {key: "機械", synonyms:  ["きかい", "機械"]},
  {key: "機会", synonyms:  ["きかい", "機かい", "機会", "き会", "キ会"]},
  {key: "き会", synonyms:  ["きかい", "機会", "き会", "キ会"]},
  {key: "キ会", synonyms:  ["きかい", "機会", "き会", "キ会"]}
]

search_volumes = {
  "きかい" => 14800,
  "機かい" => 10,
  "機械"   => 22200,
  "機会"   => 0,
  "き会"   => 0,
  "キ会"   => 0 
}

candidates = []
synonyms = []

p voice
p hiragana
p generic_words
p same_voice_tansi_lists
p search_volumes

temp = same_voice_tansi_lists.dup

# temp.delete_if{|k, v| generic_words.include?(k)}
# p temp

# 汎用語(ひらがな、カタカナ削除)
p "same_voice_tansi_lists before"
p temp
p temp[0]
p temp[0][:key]
# temp.to_a.each do |k, v|
#   temp.delete(k) and next if generic_words.include?(k)
#   temp[k] = v - generic_words
# end
# p "same_voice_tansi_lists after"
# p temp
# p "same_voice_tansi_lists count"
# p temp.size

# # 汎用語だけなら終了
# synonyms << generic_words if temp.empty?

# p "synonyms"
# p synonyms


