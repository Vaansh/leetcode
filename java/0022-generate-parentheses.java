class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        helper(n, 0, 0, "", res);
        return res;
    }

    public void helper(int n, int i, int j, String curr, List<String> res) {
        if (curr.length() == 2 * n) {
            res.add(curr);
            return;
        }

        if (i < n) {
            helper(n, i + 1, j, curr + "(", res);
        }

        if (j < i) {
            helper(n, i, j + 1, curr + ")", res);
        }
    }
}