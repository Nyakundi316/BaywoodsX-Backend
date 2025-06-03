from app import create_app
from app.extensions import db
from app.models.product import Product
from app.models.sale_product import SaleProduct
from app.models.shoes_product import ShoesProduct, ShoesProductImage
import sys
import os
from app.models.men_runner import MenRunnerProduct, MenRunnerImage

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = create_app()

with app.app_context():

    MenRunnerImage.query.delete()
    MenRunnerProduct.query.delete()
    db.session.commit()
    db.drop_all()
    db.create_all()

    products = [

        Product(
            name="Nike tns",
            category="shoes",
            price="KES 3,800",
            brand="Nike",
            color="white",
            image="https://i.pinimg.com/736x/ca/29/71/ca2971f6f94bfdf055d66bbfc7f8d1ca.jpg",
            sizes=["S", "M", "L", "XL"]
        ),
        Product(
            name="Nike tns",
            category="shoes",
            price="KES 3,800",
            brand="Baywoods",
            color="white/black",
            image="https://i.pinimg.com/736x/c8/be/d5/c8bed5f3a758f4826e142f260be47915.jpg",
            sizes=["M", "L", "XL"]
        ),
        Product(
            name="Nike Air Max",
            category="shoes",
            price="KES 3,800",
            brand="Nike",
            color="White",
            image="https://i.pinimg.com/736x/03/1d/c9/031dc91944d15b97bb202807311b7766.jpg",
            sizes=["M", "L", "XL"]
        ),
        Product(
            name="Nike Air Max",
            category="shoes",
            price="KES 3,800",
            brand="Nike",
            color="White/Gold",
            image="https://i.pinimg.com/736x/bd/f6/cd/bdf6cd604e78583f6febb2d0718d089d.jpg",
            sizes=["S", "M", "L"]
        ),
        Product(
            name="Nike Air Max tn",
            category="shoes",
            price="KES 3,600",
            brand="Nike",
            color="Grey/Neon",
            image="https://i.pinimg.com/736x/df/a5/ee/dfa5ee2e5abcbd45026216b274131042.jpg",
            sizes=["S", "M", "XL"]
        ),
        Product(
            name="Nike Air Force",
            category="shoes",
            price="KES 2800",
            brand="Nike",
            color="Black",
            image="https://i.pinimg.com/736x/75/63/7a/75637a944674b746f9b97e1bf7e8e561.jpg",
            sizes=["S", "M", "XL"]
        ),
        Product(
            name="Nike Air Force",
            category="shoes",
            price="KES 2800",
            brand="Nike",
            color="Red",
            image="https://i.pinimg.com/736x/3c/0d/15/3c0d15b1fdd36bd7c90a0bceece66718.jpg",
            sizes=["M", "L", "XL"]
        ),
        Product(
            name="Nike Air Force",
            category="shoes",
            price="KES 3800",
            brand="Nike",
            color="White",
            image="https://i.pinimg.com/736x/dc/de/93/dcde932bb5900d2049f4852fb2e6ab9b.jpg",
            sizes=["S", "M", "L"]
        ),
        Product(
            name="Nike Air Force",
            category="shoes",
            price="KES 3800",
            brand="Nike",
            color="Beige",
            image="https://i.pinimg.com/736x/21/ff/f9/21fff902488859517cffae7352956779.jpg",
            sizes=["M", "L"]
        ),
        Product(
            name="Nike Air Force",
            category="shoes",
            price="KES 2800",
            brand="Nike",
            color="White/Red",
            image="https://i.pinimg.com/736x/30/a7/8b/30a78b6e0860d040ed99e13509f8a89d.jpg",
            sizes=["S", "L", "XL"]
        ),
        # Adidas 00s
        *[
            Product(
                name="Adidas 00s",
                category="shoes",
                price="KES 3600",
                brand="Adidas",
                color=color,
                image=img,
                sizes=[str(s) for s in range(37, 45)]
            ) for color, img in [
                ("Black", "https://i.pinimg.com/736x/1f/81/74/1f81742caad3fab75350cd3f7e73b57b.jpg"),
                ("Green", "https://i.pinimg.com/736x/ef/e1/0c/efe10cfad4af7db20cf0a6454b82f2e5.jpg"),
                ("Grey", "https://i.pinimg.com/736x/ac/74/34/ac74342df449788a2d2a5920dd53a0b5.jpg"),
                ("Pink", "https://i.pinimg.com/736x/64/08/2d/64082d7d648655e6abb72e98fcc64565.jpg"),
                ("Brown", "https://i.pinimg.com/736x/a6/38/0e/a6380e8549e8f87323b82dc06f23105e.jpg"),
                ("Maroon", "https://i.pinimg.com/736x/a7/cb/ed/a7cbedbf7c0df6625b034ee364127aad.jpg"),
                ("black/white", "https://i.pinimg.com/736x/61/c1/f4/61c1f4dbd4dbb469f2451c301bf8385c.jpg"),
                ("red/white", "https://i.pinimg.com/736x/89/74/6a/89746add5442ab64b1c14c9caf0c8738.jpg"),
                ("red/grey", "https://i.pinimg.com/736x/9a/4d/eb/9a4deb42208b60619444d6c0b2c71c80.jpg"),
                ("pink/black", "https://i.pinimg.com/736x/2c/2f/82/2c2f82ea7138eeeffc114df8751d5b55.jpg"),


            ]
        ],
        # Adidas Samba
        *[
            Product(
                name="Adidas Samba",
                category="shoes",
                price="KES 4200",
                brand="Adidas",
                color=color,
                image=img,
                sizes=[str(s) for s in range(37, 45)]
            ) for color, img in [
                ("White/Black", "https://i.pinimg.com/736x/f4/9d/b4/f49db46602e8bf5ead0c1d3e962273ac.jpg"),
                ("Black/Gum", "https://i.pinimg.com/736x/86/55/4f/86554f9b2a4b547845511b3bd9dff610.jpg"),
                ("Grey", "https://i.pinimg.com/736x/d7/a0/4b/d7a04b5857f5d826e83481b928559f32.jpg"),
                ("Beige", "https://i.pinimg.com/736x/bb/5b/f8/bb5bf893531280e1d6c70676f1f56371.jpg"),
            ]
        ],
        #Adidas Double Sole
        *[
            Product(
                name="Adidas Double Sole",
                category="shoes",
                price="KES 3500",
                brand="Adidas",
                color=color,
                image=img,
                sizes=[str(s) for s in range (37, 45)]
                
            ) for color, img in [
                ("white/black", "https://i.pinimg.com/736x/ff/30/cb/ff30cb2095fef91058e4871065de428c.jpg"),
                ("white/blac", "https://i.pinimg.com/736x/b6/e6/ec/b6e6ec30df90a0d819b16ab1788bab7e.jpg"),
                ("white", "https://i.pinimg.com/736x/ac/ad/4e/acad4eabf5795d2164509006e74e93f5.jpg"),
                ("pinksole", "https://i.pinimg.com/736x/c5/90/d3/c590d3b23f559240c896d311df521925.jpg"),

            ]
        ],
        # Jordans
        *[
            Product(
                name="Air Jordan 1",
                category="shoes",
                price="KES 8500",
                brand="Jordan",
                color=color,
                image=img,
                sizes=[str(s) for s in range(37, 45)]
            ) for color, img in [
                ("Bred (Black/Red)", "https://i.pinimg.com/736x/41/f6/43/41f643143963891907660e00af6c0dd2.jpg"),
                ("Royal Blue", "https://i.pinimg.com/736x/82/aa/29/82aa2955c7b96cecae687ccb23cd54fe.jpg"),
                ("Pine Green", "https://i.pinimg.com/736x/e6/06/6b/e6066b227bada3222e835bf8cf938f03.jpg"),
                ("Shadow Grey", "https://i.pinimg.com/736x/1c/de/f7/1cdef7d35e6e54d0a2cebaa202b3b898.jpg"),
            ]
        ],
        # Vans
        *[
            Product(
                name="Vans Old Skool",
                category="shoes",
                price="KES 4200",
                brand="Vans",
                color=color,
                image=img,
                sizes=[str(s) for s in range(37, 45)]
            ) for color, img in [
                ("Black/White", "https://i.pinimg.com/736x/d1/30/59/d130596f5b9002b6f455f475971c7978.jpg"),
                ("Red/White", "https://i.pinimg.com/736x/a1/f0/79/a1f079c0d159d19e542b80f75896b383.jpg"),
                ("Blue/Gum", "https://i.pinimg.com/736x/28/95/c7/2895c7a3b16d2a506e58322bddf28dc3.jpg"),
                ("Brown/White", "https://i.pinimg.com/736x/bb/1a/1e/bb1a1e07c1017e2f3f13023e7690a4dd.jpg"),
            ]
        ],
        # New Balance
        *[
            Product(
                name="New Balance 550",
                category="shoes",
                price="KES 5000",
                brand="New Balance",
                color=color,
                image=img,
                sizes=[str(s) for s in range(37, 45)]
            ) for color, img in [
                ("White/Green", "https://i.pinimg.com/736x/ba/db/6c/badb6ce065026d9c928edf1f56db162b.jpg"),
                ("White/Red", "https://i.pinimg.com/736x/f0/24/f3/f024f3e077554a7117e53b51b6c24e4c.jpg"),
                ("Grey", "https://i.pinimg.com/736x/a0/4f/b8/a04fb8982e74f7020a3716a537d363e5.jpg"),
                ("Black", "https://i.pinimg.com/736x/ed/14/c7/ed14c7339cbb34e9b3ae8a730515c389.jpg"),
            ]
        ],
        # Nike Dunks
        *[
            Product(
                name="Nike Dunk Low",
                category="shoes",
                price="KES 6500",
                brand="Nike",
                color=color,
                image=img,
                sizes=[str(s) for s in range(37, 45)]
            ) for color, img in [
                ("Panda (Black/White)", "https://i.pinimg.com/736x/5a/35/7e/5a357e7f39cca5dc18ee7a3df8bfee26.jpg"),
                ("University Red", "https://i.pinimg.com/736x/ab/0f/a1/ab0fa12b36373a43dc5948ce11efde74.jpg"),
                ("Blue/White", "https://i.pinimg.com/736x/04/de/1f/04de1fe6322ea2c554a49d62408472f5.jpg"),
                ("White/Orange", "https://i.pinimg.com/736x/e8/09/71/e80971d2a4c4517efce7d9a60a9f2780.jpg"),
            ]
        ],
        
    ]


    sale_items = [
        SaleProduct(
            name="Retro Runners",
            category="Sneakers",
            price=11000,
            discount=20,
            colors={
                "black": [
                    "https://images.pexels.com/photos/2529148/pexels-photo-2529148.jpeg",
                    "https://images.pexels.com/photos/4041686/pexels-photo-4041686.jpeg",
                    "https://images.pexels.com/photos/4046116/pexels-photo-4046116.jpeg"
                ],
                "white": [
                    "https://images.pexels.com/photos/1445385/pexels-photo-1445385.jpeg",
                    "https://images.pexels.com/photos/298864/pexels-photo-298864.jpeg"
                ]
            }
        ),
        SaleProduct(
            name="Classic Cap",
            category="Caps",
            price=4800,
            discount=30,
            colors={
                "red": [
                    "https://images.pexels.com/photos/1584811914966-19566cfe638b.jpeg",
                    "https://images.pexels.com/photos/913862/pexels-photo-913862.jpeg"
                ],
                "blue": [
                    "https://images.pexels.com/photos/731932/pexels-photo-731932.jpeg",
                    "https://images.pexels.com/photos/998323/pexels-photo-998323.jpeg"
                ]
            }
        ),
        SaleProduct(
            name="Baywoods Hoodie",
            category="Hoodies",
            price=6500,
            discount=25,
            colors={
                "gray": [
                    "https://images.pexels.com/photos/1599058917212-d750089bc06b.jpeg",
                    "https://images.pexels.com/photos/2659662/pexels-photo-2659662.jpeg"
                ],
                "green": [
                    "https://images.pexels.com/photos/4046106/pexels-photo-4046106.jpeg",
                    "https://images.pexels.com/photos/3158823/pexels-photo-3158823.jpeg"
                ]
            }
        ),
        SaleProduct(
            name="Track Pants",
            category="Pants",
            price=7900,
            discount=15,
            colors={
                "black": [
                    "https://images.pexels.com/photos/1556715/pexels-photo-1556715.jpeg",
                    "https://images.pexels.com/photos/2442890/pexels-photo-2442890.jpeg"
                ],
                "navy": [
                    "https://images.pexels.com/photos/846741/pexels-photo-846741.jpeg",
                    "https://images.pexels.com/photos/1775983/pexels-photo-1775983.jpeg"
                ]
            }
        ),
        SaleProduct(
            name="Performance Gym Tee",
            category="Gym Wear",
            price=4200,
            discount=10,
            colors={
                "gray": [
                    "https://images.pexels.com/photos/428340/pexels-photo-428340.jpeg",
                    "https://images.pexels.com/photos/209136/pexels-photo-209136.jpeg"
                ]
            }
        ),
        
    ]

    sizes = [str(s) for s in range(37, 46)]

shoes_data = [
    (
        ShoesProduct(
            name="Nike Dunk Low",
            brand="Nike",
            category="shoes",
            price="KES 6,500",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("Panda", "https://i.pinimg.com/736x/5a/35/7e/5a357e7f39cca5dc18ee7a3df8bfee26.jpg"),
        ("University Red", "https://i.pinimg.com/736x/ab/0f/a1/ab0fa12b36373a43dc5948ce11efde74.jpg"),
    ]
] + [
    (
        ShoesProduct(
            name="Adidas Ultraboost",
            brand="Adidas",
            category="shoes",
            price="KES 14,500",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("Core Black", "https://images.unsplash.com/photo-1585386959984-a415522e3f47"),
        ("Triple White", "https://images.unsplash.com/photo-1600185366254-d4c3e21b2252"),
    ]
] + [
    (
        ShoesProduct(
            name="Yeezy Boost 350",
            brand="Yeezy",
            category="shoes",
            price="KES 28,000",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("Zebra", "https://images.unsplash.com/photo-1587019155386-bc0caef9db7f"),
        ("Carbon", "https://images.unsplash.com/photo-1580934529784-1afc82db5364"),
    ]
] + [
    (
        ShoesProduct(
            name="Air Jordan 1",
            brand="Jordan",
            category="shoes",
            price="KES 22,000",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("Chicago", "https://images.unsplash.com/photo-1600185365401-55e4e08ad6b3"),
        ("Bred", "https://images.unsplash.com/photo-1622473591862-3a0e768a6f41"),
    ]
] + [
    (
        ShoesProduct(
            name="Puma RS-X",
            brand="Puma",
            category="shoes",
            price="KES 11,800",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("Black/Blue", "https://images.unsplash.com/photo-1602288637782-4989e260ff7f"),
        ("White/Green", "https://images.unsplash.com/photo-1579338559193-94f1d5d34291"),
    ]
] + [
    (
        ShoesProduct(
            name="Vans Old Skool",
            brand="Vans",
            category="shoes",
            price="KES 7,800",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("Classic Black/White", "https://images.unsplash.com/photo-1596462502278-fcda3dbe7df1"),
        ("Red Canvas", "https://images.unsplash.com/photo-1586473219015-3e7d34287187"),
    ]
] + [
    (
        ShoesProduct(
            name="New Balance 550",
            brand="New Balance",
            category="shoes",
            price="KES 13,500",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("White/Navy", "https://images.unsplash.com/photo-1611075382035-ef2fc0f44d59"),
        ("White/Green", "https://images.unsplash.com/photo-1600185365283-2d9ee7b2f96d"),
    ]
] + [
    (
        ShoesProduct(
            name="Balenciaga Triple S",
            brand="Balenciaga",
            category="shoes",
            price="KES 72,000",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("Beige/Grey", "https://images.unsplash.com/photo-1617643824644-1734e5c62d76"),
        ("Black/Red", "https://images.unsplash.com/photo-1612245449477-2be2cb270c8f"),
    ]
] + [
    (
        ShoesProduct(
            name="Reebok Classic",
            brand="Reebok",
            category="shoes",
            price="KES 9,900",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("All White", "https://images.unsplash.com/photo-1609017903679-984bb60ed4a3"),
        ("Grey/White", "https://images.unsplash.com/photo-1583240991562-ef1f4cc98e33"),
    ]
] + [
    (
        ShoesProduct(
            name="Converse Chuck Taylor",
            brand="Converse",
            category="shoes",
            price="KES 8,500",
            color=color,
            sizes=sizes
        ),
        img
    )
    for color, img in [
        ("Black Canvas", "https://images.unsplash.com/photo-1605052511925-33ed480a90a2"),
        ("White Canvas", "https://images.unsplash.com/photo-1612423284934-e8fd9f3b3df0"),
    ]
],

runners = [
    {
        "name": "Nike Air Max 90",
        "brand": "Nike",
        "category": "shoes",
        "price": 12999.00,
        "images": [
            "https://images.unsplash.com/photo-1606813902526-0663b653f075",
            "https://images.unsplash.com/photo-1606814020228-79bb54fdefe6"
        ]
    },
    {
        "name": "Adidas Ultraboost",
        "brand": "Adidas",
        "category": "shoes",
        "price": 13999.00,
        "images": [
            "https://images.unsplash.com/photo-1606811842409-1c134d9de7f3",
            "https://images.unsplash.com/photo-1606811842352-13416b4d9980"
        ]
    }
]



with app.app_context():
    # ✅ Seed ShoesProduct + ShoesProductImage
    if not ShoesProduct.query.first():
        print("⏳ Seeding shoes and images...")

        for shoe_data in runners:
            shoe = ShoesProduct(
                name=shoe_data["name"],
                brand=shoe_data["brand"],
                price=shoe_data["price"],
                category=shoe_data["category"]
            )
            db.session.add(shoe)
            db.session.flush()

            for img_url in shoe_data["images"]:
                image = ShoesProductImage(url=img_url, product_id=shoe.id)
                db.session.add(image)

        db.session.commit()
        print("✅ Seeded all shoes successfully.")
    else:
        print("⚠️ Shoes already seeded. Skipping.")

    # ✅ Seed Product + SaleProduct + MenRunnerProduct + MenRunnerImage
    if not products or not sale_items:
        print("⚠️ No products or sale items to seed.")
    else:
        if not MenRunnerProduct.query.first():
            print("⏳ Seeding men runners with color images...")

            for item in runners:
                product = MenRunnerProduct(
                    name=item["name"],
                    brand=item["brand"],
                    category=item["category"],
                    price=item["price"]
                )
                db.session.add(product)
                db.session.flush()

                for url in item["images"]:  # ✅ This works with list of URLs
                    db.session.add(MenRunnerImage(
                        url=url,
                        product_id=product.id
                    ))


            db.session.bulk_save_objects(products)
            db.session.add_all(sale_items)
            db.session.commit()

            print("✅ Seeded all products successfully.")
            print("✅ Seeded 20 images across SaleProducts successfully.")
            print("✅ Seeded Men Runners with images by color.")
        else:
            print("⚠️ Products already seeded. Skipping.")

    print("✅ Seeding complete.")
