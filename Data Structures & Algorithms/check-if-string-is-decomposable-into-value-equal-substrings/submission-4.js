class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isDecomposable(s) {
        let length_2_block = 0;
        let pointer_1 = 1;
        let cur_group_len = 1;
        while (pointer_1 <=s.length-1){
            let prev_char = s[pointer_1-1];
            let cur_char = s[pointer_1];
            if (prev_char == cur_char){
                cur_group_len+=1;
            }else{
                if(cur_group_len%3==1){
                    return false
                }if (cur_group_len % 3 == 2){
                    length_2_block +=1;
                }
               cur_group_len = 1; 
            }pointer_1+=1;
        }
        if (cur_group_len % 3 == 1){
            return false
        }
        if(cur_group_len % 3 == 2){
            length_2_block += 1
        }
    if (length_2_block == 1){
        return true
    }else{
        return false
    }
    }
}
