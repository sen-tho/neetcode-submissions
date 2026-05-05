class Solution {

    public String encode(List<String> strs) {
        String encoded="";
        for(int i = 0; i < strs.size(); ++i)
        {
            encoded+= strs.get(i) + '\u0000';
        }
        System.out.print(encoded);
        return encoded;
    }

    public List<String> decode(String str) {
        String word="";
        List<String> decoded_list = new ArrayList<String>();

        for(int  i = 0; i < str.length(); ++i){
            if(str.charAt(i) == '\u0000'){
                decoded_list.add(word);
                word = "";
            }
            else word+= str.charAt(i);
        }
        return decoded_list;
    }
}
