import java.util.*;

class Element {
    int key;
    int freq;
    
    Element(int key, int freq) {
        this.key = key;
        this.freq = freq;
    }
}

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        PriorityQueue<Element> pq = new PriorityQueue<>((e1, e2) -> e2.freq - e1.freq);
        for (var entry : map.entrySet()) {
            pq.add(new Element(entry.getKey(), entry.getValue()));
        }

        int i = 0;
        int[] res = new int[k];
        while (!pq.isEmpty() && i < k) {
            res[i] = pq.poll().key;
            i++;
        }

        return res;
    }
}

// class Solution {
//     public int[] topKFrequent(int[] nums, int k) {
//         HashMap<Integer, Integer> map = new HashMap<>();
//         for (int n : nums) {
//             map.put(n, map.getOrDefault(n, 0) + 1);
//         }
//         List<Integer> list = new ArrayList<>(map.keySet());
//         Collections.sort(list, (a, b) -> map.get(b) - map.get(a));
//         int[] res = new int[k];
//         for (int i = 0; i < k; i++) {
//             res[i] = list.get(i);
//         }
//         return res;
//     }
// }

// class Solution {
//     public int[] topKFrequent(int[] nums, int k) {
//         HashMap<Integer, Integer> map = new HashMap<>();
//         for (int n : nums) {
//             map.put(n, map.getOrDefault(n, 0) + 1);
//         }
//         List<Integer> res = map.entrySet().stream()
//             .sorted((e1, e2) -> Integer.compare(e2.getValue(), e1.getValue()))
//             .limit(k)
//             .map(e -> e.getKey())
//             .collect(Collectors.toList());
//         int[] result = new int[res.size()];
//         for (int i = 0; i < res.size(); i++) {
//             result[i] = res.get(i);
//         }
//         return result;
//     }
// }