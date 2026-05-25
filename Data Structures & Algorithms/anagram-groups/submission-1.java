class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs==null || strs.length==0){
            return new ArrayList<>();
        }
        List<List<String>> answer = new ArrayList<>();
        List<String> uniq = new ArrayList<>();
        for (int k=0;k<strs.length;k++){
            if (uniq.size()==0){
                uniq.add(strs[k]);
                List<String> firstGrp = new ArrayList<>();
                firstGrp.add(strs[k]);
                answer.add(firstGrp);
                continue;
            }else{
                int i =0;
                while (i<uniq.size()){
                    if (isAnagram(uniq.get(i),strs[k])){
                        answer.get(i).add(strs[k]);
                        break;
                    }
                    i++;
                }
                if (i>=uniq.size()){
                    uniq.add(strs[k]);
                    List<String> grp = new ArrayList<>();
                    grp.add(strs[k]);
                    answer.add(grp);
                }
            }
        }
        return answer;
    }
    public boolean isAnagram(String s, String t){
        if (s.length()!=t.length()){
            return false;
        }
        int[] chars = new int[26];
        for (int k=0;k<s.length();k++){
            chars[s.charAt(k)-'a']++;
            chars[t.charAt(k)-'a']--;
        }
        for (int k=0;k<chars.length;k++){
            if (chars[k]!=0){
                return false;
            }
        }
        return true;
    }
}
