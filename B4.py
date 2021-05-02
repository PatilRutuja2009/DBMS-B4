> db.movie.find().pretty()
{
    "_id" : ObjectId("5d92cb387e445733060279fc"),
    "Movie_id" : 101,
    "User_id" : 1,
    "Title" : "Toy Story(1995)",
    "Status" : "A",
    "Rating" : 4
}
{
    "_id" : ObjectId("5d92cb587e445733060279fd"),
    "Movie_id" : 102,
    "User_id" : 2,
    "Title" : "ice-age(2005)",
    "Status" : "A",
    "Rating" : 4.5
}
{
    "_id" : ObjectId("5d92cbad7e445733060279fe"),
    "Movie_id" : 103,
    "User_id" : 3,
    "Title" : "Fast & Furious:Hobbs & shaw(2019)",
    "Status" : "A",
    "Rating" : 5
}
{
    "_id" : ObjectId("5d92cc0c7e445733060279ff"),
    "Movie_id" : 104,
    "User_id" : 4,
    "Title" : "Avengers:End Game(2019)",
    "Status" : "P",
    "Rating" : 5
}
{
    "_id" : ObjectId("5d92cc357e44573306027a00"),
    "Movie_id" : 105,
    "User_id" : 5,
    "Title" : "Captain Marvel(2018)",
    "Status" : "A",
    "Rating" : 3
}
{
    "_id" : ObjectId("5d92cc6b7e44573306027a01"),
    "Movie_id" : 106,
    "User_id" : 6,
    "Title" : "The Conjuring(2018)",
    "Status" : "A",
    "Rating" : 3.5
}
{
    "_id" : ObjectId("5d92ccd47e44573306027a02"),
    "Movie_id" : 205,
    "User_id" : 100,
    "Title" : "The Mask(2007)",
    "Status" : "P",
    "Rating" : 3.5
}
{
    "_id" : ObjectId("5d92ccff7e44573306027a03"),
    "Movie_id" : 115,
    "User_id" : 210,
    "Title" : "Fast & furious(2007)",
    "Status" : "A",
    "Rating" : 5
}
{
    "_id" : ObjectId("5d92cd2d7e44573306027a04"),
    "Movie_id" : 205,
    "User_id" : 350,
    "Title" : "The Mask(2007)",
    "Status" : "P",
    "Rating" : 4.5
}
{
    "_id" : ObjectId("5d92cd587e44573306027a05"),
    "Movie_id" : 205,
    "User_id" : 150,
    "Title" : "The Mask(2007)",
    "Status" : "P",
    "Rating" : 3.5
}
> db.movie.dropIndexes()
{
    "nIndexesWas" : 2,
    "msg" : "non-_id indexes dropped for collection",
    "ok" : 1
}
> db.movie.ensureIndex({"Movie_id":1})
> db.movie.find().explain()
{
    "cursor" : "BasicCursor",
    "isMultiKey" : false,
    "n" : 10,
    "nscannedObjects" : 10,
    "nscanned" : 10,
    "nscannedObjectsAllPlans" : 10,
    "nscannedAllPlans" : 10,
    "scanAndOrder" : false,
    "indexOnly" : false,
    "nYields" : 0,
    "nChunkSkips" : 0,
    "millis" : 0,
    "indexBounds" : {
        
    },
    "server" : "localhost.localdomain:27017"
}
> db.movie.getIndexes()
[
    {
        "v" : 1,
        "key" : {
            "_id" : 1
        },
        "ns" : "parvej.movie",
        "name" : "_id_"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : 1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_1"
    }
]
> db.movie.find().pretty().sort({"Movie_id":-1})
{
    "_id" : ObjectId("5d92cd587e44573306027a05"),
    "Movie_id" : 205,
    "User_id" : 150,
    "Title" : "The Mask(2007)",
    "Status" : "P",
    "Rating" : 3.5
}
{
    "_id" : ObjectId("5d92cd2d7e44573306027a04"),
    "Movie_id" : 205,
    "User_id" : 350,
    "Title" : "The Mask(2007)",
    "Status" : "P",
    "Rating" : 4.5
}
{
    "_id" : ObjectId("5d92ccd47e44573306027a02"),
    "Movie_id" : 205,
    "User_id" : 100,
    "Title" : "The Mask(2007)",
    "Status" : "P",
    "Rating" : 3.5
}
{
    "_id" : ObjectId("5d92ccff7e44573306027a03"),
    "Movie_id" : 115,
    "User_id" : 210,
    "Title" : "Fast & furious(2007)",
    "Status" : "A",
    "Rating" : 5
}
{
    "_id" : ObjectId("5d92cc6b7e44573306027a01"),
    "Movie_id" : 106,
    "User_id" : 6,
    "Title" : "The Conjuring(2018)",
    "Status" : "A",
    "Rating" : 3.5
}
{
    "_id" : ObjectId("5d92cc357e44573306027a00"),
    "Movie_id" : 105,
    "User_id" : 5,
    "Title" : "Captain Marvel(2018)",
    "Status" : "A",
    "Rating" : 3
}
{
    "_id" : ObjectId("5d92cc0c7e445733060279ff"),
    "Movie_id" : 104,
    "User_id" : 4,
    "Title" : "Avengers:End Game(2019)",
    "Status" : "P",
    "Rating" : 5
}
{
    "_id" : ObjectId("5d92cbad7e445733060279fe"),
    "Movie_id" : 103,
    "User_id" : 3,
    "Title" : "Fast & Furious:Hobbs & shaw(2019)",
    "Status" : "A",
    "Rating" : 5
}
{
    "_id" : ObjectId("5d92cb587e445733060279fd"),
    "Movie_id" : 102,
    "User_id" : 2,
    "Title" : "ice-age(2005)",
    "Status" : "A",
    "Rating" : 4.5
}
{
    "_id" : ObjectId("5d92cb387e445733060279fc"),
    "Movie_id" : 101,
    "User_id" : 1,
    "Title" : "Toy Story(1995)",
    "Status" : "A",
    "Rating" : 4
}
> db.movie.ensureIndex({"Movie_id":-1})
> db.movie.aggregate([{$match:{Title:"The Mask(2007)"}},{$group:{_id:"$Movie_id",Total:{$sum:"$Rating"}}}])
{ "result" : [ { "_id" : 205, "Total" : 11.5 } ], "ok" : 1 }
> db.movie.aggregate([{$match:{Title:"ice-age(2005)"}},{$group:{_id:"$Movie_id",Total:{$sum:"$Rating"}}}])
{ "result" : [ { "_id" : 102, "Total" : 4.5 } ], "ok" : 1 }
> db.movie.reIndex({"Rating":1})
{
    "nIndexesWas" : 3,
    "msg" : "indexes dropped for collection",
    "nIndexes" : 3,
    "indexes" : [
        {
            "key" : {
                "_id" : 1
            },
            "ns" : "parvej.movie",
            "name" : "_id_"
        },
        {
            "key" : {
                "Movie_id" : 1
            },
            "ns" : "parvej.movie",
            "name" : "Movie_id_1"
        },
        {
            "key" : {
                "Movie_id" : -1
            },
            "ns" : "parvej.movie",
            "name" : "Movie_id_-1"
        }
    ],
    "ok" : 1
}
> db.movie.ensureIndex({"Movie_id":1},{"Rating":-1})
> db.movie.ensureIndex({"Movie_id":1},{"Rating":-1}).getIndexes()
Tue Oct  1 10:31:37.666 TypeError: Cannot call method 'getIndexes' of undefined
> db.movie.getIndexes()
[
    {
        "v" : 1,
        "key" : {
            "_id" : 1
        },
        "ns" : "parvej.movie",
        "name" : "_id_"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : 1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_1"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : -1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_-1"
    }
]
> db.movie.ensureIndex({"Movie_id":1,"Rating":-1})
> db.movie.getIndexes()
[
    {
        "v" : 1,
        "key" : {
            "_id" : 1
        },
        "ns" : "parvej.movie",
        "name" : "_id_"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : 1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_1"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : -1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_-1"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : 1,
            "Rating" : -1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_1_Rating_-1"
    }
]
> db.movie.ensureIndex({"Movie_id":1,"User_id":1,"Rating":-1})
> db.movie.getIndexes()
[
    {
        "v" : 1,
        "key" : {
            "_id" : 1
        },
        "ns" : "parvej.movie",
        "name" : "_id_"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : 1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_1"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : -1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_-1"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : 1,
            "Rating" : -1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_1_Rating_-1"
    },
    {
        "v" : 1,
        "key" : {
            "Movie_id" : 1,
            "User_id" : 1,
            "Rating" : -1
        },
        "ns" : "parvej.movie",
        "name" : "Movie_id_1_User_id_1_Rating_-1"
    }
]
> db.movie.find().limit().pretty()
{
    "_id" : ObjectId("5d92cb387e445733060279fc"),
    "Movie_id" : 101,
    "User_id" : 1,
    "Title" : "Toy Story(1995)",
    "Status" : "A",
    "Rating" : 4
}
{
    "_id" : ObjectId("5d92cb587e445733060279fd"),
    "Movie_id" : 102,
    "User_id" : 2,
    "Title" : "ice-age(2005)",
    "Status" : "A",
    "Rating" : 4.5
}
{
    "_id" : ObjectId("5d92cbad7e445733060279fe"),
    "Movie_id" : 103,
    "User_id" : 3,
    "Title" : "Fast & Furious:Hobbs & shaw(2019)",
    "Status" : "A",
    "Rating" : 5
}
{
    "_id" : ObjectId("5d92cc0c7e445733060279ff"),
    "Movie_id" : 104,
    "User_id" : 4,
    "Title" : "Avengers:End Game(2019)",
    "Status" : "P",
    "Rating" : 5
}
{
    "_id" : ObjectId("5d92cc357e44573306027a00"),
    "Movie_id" : 105,
    "User_id" : 5,
    "Title" : "Captain Marvel(2018)",
    "Status" : "A",
    "Rating" : 3
}
{
    "_id" : ObjectId("5d92cc6b7e44573306027a01"),
    "Movie_id" : 106,
    "User_id" : 6,
    "Title" : "The Conjuring(2018)",
    "Status" : "A",
    "Rating" : 3.5
}
{
    "_id" : ObjectId("5d92ccd47e44573306027a02"),
    "Movie_id" : 205,
    "User_id" : 100,
    "Title" : "The Mask(2007)",
    "Status" : "P",
    "Rating" : 3.5
}
{
    "_id" : ObjectId("5d92ccff7e44573306027a03"),
    "Movie_id" : 115,
    "User_id" : 210,
    "Title" : "Fast & furious(2007)",
    "Status" : "A",
    "Rating" : 5
}
{
    "_id" : ObjectId("5d92cd2d7e44573306027a04"),
    "Movie_id" : 205,
    "User_id" : 350,
    "Title" : "The Mask(2007)",
    "Status" : "P",
    "Rating" : 4.5
}
{
    "_id" : ObjectId("5d92cd587e44573306027a05"),
    "Movie_id" : 205,
    "User_id" : 150,
    "Title" : "The Mask(2007)",
    "Status" : "P",
    "Rating" : 3.5
}
> db.movie.dropIndexes()
{
    "nIndexesWas" : 2,
    "msg" : "non-_id indexes dropped for collection",
    "ok" : 1
}
