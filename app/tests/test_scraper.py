import os

from app.utils.scraper.origin_scrape import supermarkets_scrape

def read_html():
      relative_path = '../utils/sainsburys.html'
      absolute_path = os.path.abspath(relative_path)
      with open(absolute_path) as file:
        return file.read()

def scraper_test():
    expectedNames = ['Strong Roots Oven Baked Sweet Potato 500g', 'Alpro Almond No Sugars Long Life Drink 1L', 'Alpro Almond No Sugars Chilled Drink 1L', 'Vitalite Dairy Free Spread 500g', 'Heck British Chicken Italia Sausages 340g', 'Alpro No Bits Strawberry Banana & Peach Pear Yogurt Alternative 4x125g', 'The Coconut Collaborative Natural Yogurt Alternative 350g', 'Alpro Soya Yofu Red Fruit Mix Blueberry & Cherry 4x125g', 'Alpro Plain Unsweetened No Sugars Plant-Based Alternative To Yoghurt 500g', 'Quorn Vegan Smoky Ham Free Slices 100g', "Sainsbury's Deliciously Free From Fusilli 500g", "Sainsbury's Deliciously Free From Penne 500g", 'Alpro Soya No Sugars Chilled Drink 1L', 'Alpro Soya Vanilla Flavoured 500g', 'Alpro Plain with Coconut Yoghurt Alternative 500g', 'Alpro Soya Chilled Drink 1L', 'Heck 97% British Pork Sausages 400g', "Sainsbury's Deliciously Free From Oats 450g", 'Eat Real Lentil Chips Sea Salt Flavour 113g', 'Swedish Glace Vanilla Dairy Free Vegan Ice Cream Tub Dessert 750ml', 'Warburtons Gluten Free Super Soft Sliced Square Rolls x4 240g', 'Alpro Soya Long Life Drink 1L', 'Alpro Dark Chocolate Dessert 4x125g', 'Kallo Dark Chocolate Rice Cake Thins Gluten Free 90g', "Sainsbury's Fresh British Turkey Gluten Free Sausages x8 454g", 'Schar Gluten Free Wholesome Seeded Loaf 300g', 'Alpro No Sugars Organic Soya Long Life Drink 1L', "Sainsbury's Deliciously Free From Chocolate Chip Cookies 150g", 'Alpro Rasberry Cranberry & Blackberry Yogurt Alternative 4x125g', "Nairn's Chocolate Biscuit Breaks 160g", 'Manomasa Manchego & Green Olive Sharing Tortilla Chips 140g', 'Alpro Soya No Sugars Long Life Drink 1L', "Sainsbury's Deliciously Free From Spaghetti 500g", "Hellmann's Plant Based Vegan Mayonnaise 270g", 'Warburtons Tiger Artisan Bloomer, Gluten Free 400g', 'Warburtons Gluten Free Multiseed Loaf 300g ', 'BOL Garden Pea & Spinach Protein Power Soup', "Goodfella's Gluten Free Pepperoni Pizza 317g", 'Eat Real Hummus, Lentil, Quinoa Chips X5 116g', "Sacla' Vegan Basil Pesto 190g", 'Clearspring Organic Japanese Silken & Smooth Tofu 300g', 'Warburtons Gluten Free White Bread Sourdough 400g', 'Birds Eye Gluten Free Breaded Fish Fingers x12 360g', 'Alpro Soya Long Life Alternative to Single Cream 250ml ', "Sainsbury's Red Lentil Penne 250g", 'Alpro greek Style Strawberry & Raspberry Yogurt Alternative 150g', 'Alpro Vanilla Custard 525g', 'Rude Health Almond Drink 1L', 'Alpro Smooth Chocolate Dessert 4x125g', "Nairn's Gluten Free Scottish Porridge Oats 450g", 'BOL Butternut Squash & Chilli Immunity Power Soup', 'Alpro Soya Growing Up Long Life Drink 1L', 'Rude Health Oat Drink 1L', 'Alpro Plain Yoghurt Alternative 500g ', 'Nairns Gluten Free Oatcakes 213g', "Mrs Crimble's Gluten Free Coconut Macaroons x6", 'Alpro Almond Long Life Drink 1L', 'Promise Gluten Free Multigrain Loaf 480g', "Sainsbury's Little Ones Organic Apple & Blueberry Rice Cakes 12+ Months 40g", "Sainsbury's Little Ones Organic Apple Rice Cakes 12+ Months 40g"]
    expectedUrls = ['https://assets.sainsburys-groceries.co.uk/gol/7934004/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7595669/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7603414/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7284376/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7792825/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/3486788/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7783545/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7227349/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7881758/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7898419/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7782881/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7782809/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7223524/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7063455/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7740228/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/3979624/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7792830/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7783244/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7894465/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/2486123/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/8061231/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/2654737/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7213894/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/3443903/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7839772/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7873267/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/2654720/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7783517/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7749493/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7671002/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7754631/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/2967684/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7782893/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7936618/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7857744/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/8013508/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/8180762/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7861899/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7894469/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7688449/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7745153/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7746118/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7833673/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/2939735/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7967268/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7847452/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7139025/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7651481/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/2813578/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7745300/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/8180766/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7501422/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7651490/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/3071953/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7510765/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/6413097/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/7544271/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/8032550/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/8120464/image.jpg', 'https://assets.sainsburys-groceries.co.uk/gol/8120472/image.jpg'] 
    
    scrapedData = supermarkets_scrape(read_html())
   
    assert scrapedData == (expectedNames, expectedUrls)

scraper_test()