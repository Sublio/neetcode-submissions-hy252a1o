class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    maxLengthBetweenEqualCharacters(s) {
        const cnt = {};
        for (const c of s) cnt[c] = (cnt[c] ?? 0) + 1;
        let maxSeen = 0;
        for (const [c, v] of Object.entries(cnt)) {
            if (v > 1) {
                const indices = [];
                for (let i = 0; i < s.length; i++) {
                    if (s[i] === c) indices.push(i);
                }
                maxSeen = Math.max(maxSeen, Math.max(...indices) - Math.min(...indices));
        }
    }
    return maxSeen - 1;
    }
}
