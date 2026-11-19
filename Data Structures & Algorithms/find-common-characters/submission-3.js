class Solution {
    /**
     * @param {string[]} words
     * @return {string[]}
     */
    commonChars(words) {
        const alphabet = "abcdefghijklmnopqrstuvwxyz";
        let res = []
        for (const c of alphabet){
            let cur_char_counters = []
            for (const word of words){
                if (word.includes(c)){
                    let word_cnt = 0;
                    for (const ch of word) {
                        if (ch === c) word_cnt++;
                    }
                    cur_char_counters.push(word_cnt);
                }else{
                    cur_char_counters = []
                    break;
                }
            }
            if (cur_char_counters.length > 0) {
                const n = Math.min(...cur_char_counters);
                res.push(...Array(n).fill(c));
            }
        }

        return res
        
    }
}

    // def commonChars(self, words: List[str]) -> List[str]:
    //     import string
    //     alphabet = string.ascii_lowercase
    //     res = []
    //     for c in alphabet:
    //         cur_char_counters = []
    //         for word in words:
    //             if c in word:
    //                 word_cnt = Counter(word)[c]
    //                 cur_char_counters.append(word_cnt)
    //             else:
    //                 cur_char_counters = []
    //                 break
    //         if cur_char_counters:
    //             res.extend(min(cur_char_counters)*c)

    //     return res
