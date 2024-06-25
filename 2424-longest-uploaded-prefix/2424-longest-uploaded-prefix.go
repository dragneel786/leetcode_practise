type LUPrefix struct {
    curr int
    hashSet map[int]bool
}


func Constructor(n int) LUPrefix {
    return LUPrefix{
        curr: 0,
        hashSet: make(map[int]bool),
    }
}


func (this *LUPrefix) Upload(video int)  {
    var pref = this.hashSet
    pref[video] = true
    for this.hashSet[this.curr + 1] {
        this.curr++
    }
}


func (this *LUPrefix) Longest() int {
    return this.curr
}


/**
 * Your LUPrefix object will be instantiated and called as such:
 * obj := Constructor(n);
 * obj.Upload(video);
 * param_2 := obj.Longest();
 */