#Accesing Items from a Dictionary 

dict =[
{
   "Model":"2022",
   "Brand":"Honda",
   "Year":"2022-01-10"
},
{
   "Model":"2023",
   "Brand":"Toyota",
   "Year":"2023-01-10"
},
{
   "Model":"2021",
   "Brand":"Suzuki",
   "Year":"2021-05-10"
}
]

for c in dict:

    a=c["Year"].split("-")[0]
    b=c["Year"].split("-")[1]
    r=c["Year"].split("-")[2]
    print(a) 
    print(b)
    print(r)

   



