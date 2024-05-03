func compareVersion(version1 string, version2 string) int {
  splits1 := strings.Split(version1, ".")
  splits2 := strings.Split(version2, ".")
  maxLen := max(len(splits1), len(splits2))
  for i := range maxLen{
      val1 := 0
      if i < len(splits1){
          val1, _ = strconv.Atoi(splits1[i])
      }
      
      val2 := 0
      if i < len(splits2){
          val2, _ = strconv.Atoi(splits2[i])
      }
      if val1 < val2 {
          return -1
      } else if val1 > val2 {
          return 1
      }
      
  }
  return 0
}