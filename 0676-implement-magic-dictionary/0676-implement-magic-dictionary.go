	// Online Go compiler to run Golang program online
// Print "Hello, World!" message

package main
import "fmt"

type TrieNode struct {
	children map[rune]*TrieNode
	isEnd bool
}

type MagicDictionary struct {
	root *TrieNode
}


func Constructor() MagicDictionary {
	return MagicDictionary{root: &TrieNode { children: make(map[rune]*TrieNode)}}
}


func (this *MagicDictionary) BuildDict(dictionary []string)  {
    node := this.root;
    for _, word := range dictionary {
        temp := node
        for _, char := range word {
            if _, ok := temp.children[char]; !ok {
                temp.children[char] = &TrieNode { children: make(map[rune]*TrieNode)};
            }
            temp = temp.children[char]
        }
        temp.isEnd = true
    }
}

func (this *MagicDictionary) Search(searchWord string) bool {
	return traverse(this.root, searchWord, 1)
}

func traverse(node *TrieNode, word string, modifiedCount int) bool{
	if modifiedCount < 0{
		return false
	}

	if len(word) == 0 {
		return modifiedCount == 0 && node.isEnd
	}

	for key, value := range node.children {
		if string(key) == string(word[0]) {
			if traverse(value, word[1:], modifiedCount){
				return true
			}
		} else {
			if traverse(value, word[1:], modifiedCount - 1){
				return true
			}
		}
	}
	return false
}