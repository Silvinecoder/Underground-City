INSERT INTO attribute (attribute_uuid, attribute_type) VALUES
('5ddf34ac-a0ed-4042-869d-d584fd10b97b','gluten-free'),
('da389ab1-7f0b-428f-bfb0-407a5c68fead','peanut allergy'),
('3b6326a1-b0f2-402c-930b-421327acbc67','lactose intolerance');

INSERT INTO category (category_uuid, category_name) VALUES
('8250b741-8948-471f-9350-bfcc0f37c8d5','bread'),
('a3e179c1-9e9b-4105-94c3-821216551a03','liquid'),
('99255e5a-d621-42b1-adc8-297755eb23a4','meat');

INSERT INTO product (product_uuid, product_name, product_image, product_attribute_uuid, product_category_uuid) VALUES
('b973cb3a-777e-44e4-8a53-f868932f8eb4','Milk','https://assets.sainsburys-groceries.co.uk/gol/357937/1/300x300.jpg','5ddf34ac-a0ed-4042-869d-d584fd10b97b','8250b741-8948-471f-9350-bfcc0f37c8d5'),
('bce06d64-3ad3-4ab1-942a-84211afdea70','water','https://assets.sainsburys-groceries.co.uk/gol/357937/1/300x300.jpg','da389ab1-7f0b-428f-bfb0-407a5c68fead','a3e179c1-9e9b-4105-94c3-821216551a03'),
('b7c950ff-3649-4124-a88d-7eba28a88036','Bread','https://assets.sainsburys-groceries.co.uk/gol/357937/1/300x300.jpg','3b6326a1-b0f2-402c-930b-421327acbc67','99255e5a-d621-42b1-adc8-297755eb23a4');

INSERT INTO supermarket (supermarket_uuid, supermarket_name, supermarket_country) VALUES
('c3dc5c28-afc4-4680-9fd6-b39132f82612','Sainsburys','UK'),
('058e6b43-4b66-4b7f-b18a-b861830a1703','Tesco','UK'),
('fadf51d4-30c4-42f8-82e5-6ce8bb6c7fb3','Asda','UK');

INSERT INTO supermarket_product_pair (supermarket_product_pair_uuid, product_uuid, supermarket_uuid) VALUES
('b787c508-76dd-4c1f-4bd0-f51b8dc3b6f9','b973cb3a-777e-44e4-8a53-f868932f8eb4','c3dc5c28-afc4-4680-9fd6-b39132f82612'),
('b787c508-76dd-4c1f-4bd0-f51b8dc3b6b9','bce06d64-3ad3-4ab1-942a-84211afdea70','058e6b43-4b66-4b7f-b18a-b861830a1703'),
('cfa52d0d-43db-dac6-fda4-59d1f49acacb','b7c950ff-3649-4124-a88d-7eba28a88036','fadf51d4-30c4-42f8-82e5-6ce8bb6c7fb3');


