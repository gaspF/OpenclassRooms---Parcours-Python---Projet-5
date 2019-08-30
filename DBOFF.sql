CREATE DATABASE DBOFF;
USE DBOFF;

  -- TABLE : product
  CREATE TABLE product (
      id INT UNSIGNED AUTO_INCREMENT NOT NULL,
      product_name VARCHAR(800) NOT NULL,
      category_name VARCHAR(500) DEFAULT NULL,
      category_id int(6) unsigned DEFAULT NULL,
      nutrition_grade CHAR(1) NOT NULL,
      product_url TEXT NOT NULL,
      product_store VARCHAR(200) DEFAULT NULL,
      PRIMARY KEY (id)
  );

  -- TABLE : category
  CREATE TABLE category (
      id INT UNSIGNED AUTO_INCREMENT NOT NULL,
      category_name VARCHAR(150) NOT NULL,
      PRIMARY KEY (id)
  );

  -- TABLE : substitute
  CREATE TABLE substitute (
      saved_product_id INT NOT NULL,
      saved_product_name VARCHAR(800) NOT NULL,
      saved_product_grade CHAR(1) NOT NULL,
      saved_substitute_id INT NOT NULL,
      saved_substitute_name VARCHAR(800) NOT NULL,
      saved_substitute_grade CHAR(1) NOT NULL
      );

  -- TABLE : category_products
  CREATE TABLE category_products (
  	  product_id INT UNSIGNED,
  	  category_id INT UNSIGNED
  	  -- primary key (couple)
  );


-- CREATE FOREIGN KEY

    -- FK category_products : product_id
    ALTER TABLE category_products
    ADD CONSTRAINT fk_cat_prod_product_id FOREIGN KEY (product_id) REFERENCES product(id);

    -- FK category_product : category_id
    ALTER TABLE category_products
    ADD CONSTRAINT fk_cat_prod_category_id FOREIGN KEY (category_id) REFERENCES category(id);

    -- FK substitute :  substitute_product_id (fk : nom de table _ id)
    ALTER TABLE substitute
    ADD CONSTRAINT fk_sav_prod_product_id FOREIGN KEY (saved_product_id) REFERENCES product(id);

    -- FK substitute : substitute_substitute_id
    ALTER TABLE substitute
    ADD CONSTRAINT fk_sav_subs_product_id FOREIGN KEY (saved_substitute_id) REFERENCES product(id);


-- CREATE INDEXES

    -- Index category : category_name
    ALTER TABLE category
    ADD INDEX ind_cat_name (category_name);

    -- Index product : product_name
    ALTER TABLE product
    ADD INDEX ind_product_name (product_name);