-- Table: public.goods

-- DROP TABLE public.goods;

CREATE TABLE public.goods
(
  article_number integer NOT NULL,
  title text,
  retail_price integer,
  weight_per_package integer,
  date_of_creation date,
  update_date date,
  cost_price integer,
  category text,
  color text,
  stock text,
  CONSTRAINT goods_article_number_key UNIQUE (article_number)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.goods
  OWNER TO postgres;
