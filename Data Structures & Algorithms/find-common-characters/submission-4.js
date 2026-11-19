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
