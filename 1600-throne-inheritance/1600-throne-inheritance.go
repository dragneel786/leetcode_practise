type ThroneInheritance struct {
  head string;
  deaths map[string]bool;
  childrens map[string][]string;
}


func Constructor(kingName string) ThroneInheritance {
  throneIn := ThroneInheritance{
      head: kingName,
      deaths: make(map[string]bool),
      childrens: make(map[string][]string),
  }
  return throneIn 
}


func (this *ThroneInheritance) Birth(parentName string, childName string)  {
  childrens := this.childrens
  if _, exist := childrens[parentName]; !exist {
      childrens[parentName] = []string{}
  }
  childrens[parentName] = append(childrens[parentName], childName)
}


func (this *ThroneInheritance) Death(name string)  {
  this.deaths[name] = true
}


func (this *ThroneInheritance) GetInheritanceOrder() []string {
  king := this.head
  deaths := this.deaths
  childrens := this.childrens
  order := []string{}
  inheritOrder(king, &deaths, &childrens, &order)
  return order
}


func inheritOrder(node string, deaths *map[string]bool, childrens *map[string][]string, order *[]string) {
  
    if !(*deaths)[node] {
      *order = append(*order, node)
  }
  
    for _, child := range (*childrens)[node] {
      inheritOrder(child, deaths, childrens, order)
  }
}