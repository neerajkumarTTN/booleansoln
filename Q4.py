products= {
    "fruits"    :{
        "banan" :10,
        "apple" :20,
        "cherry":30
    },
    "staionary":{
        "pen"  :5,
        "book" :50,
        "copy" :15,
    }
}
print(products)
x=products.get("fruits")
print(x)
for key in x.items():
    print(list(key))