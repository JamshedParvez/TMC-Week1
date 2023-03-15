jdict ={
   
   "Model":"2022",
   "Brand":"Honda",
   "Year":"2022-01-10"
}

#jdict.pop("Brand")
#print(jdict)

thisdict={
      "Model":"2020",
   "Brand":"Suzuki",
   "Year":"2020-04-20"
}

dict1={
   "Model":"2021",
   "Brand":"Toyota",
   "Year":"2021-08-26"
}

dictNew = {
   
   "Child1":jdict,
   "Child2":thisdict,
   "Child3":dict1,

}

print(dictNew)
print(dictNew.keys())

dictNew.pop("Child1")
print(dictNew)
