
function lengthOfLongestSubstring(s: string): number {
    let map= new Map<string, number>()
    
    let left = 0
    let maxLength = 0 

    for (let right= 0 ; right<s.length; right++){
        const char = s[right]

        if (map.has(char) && map.get(char) >= left){
            left = map.get(char) +1
        }

        map.set(char, right)

        maxLength = Math.max(
            maxLength,
            right - left + 1
        )
    }
    return maxLength

};