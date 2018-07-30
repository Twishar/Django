-- Table: public.goods_goods

-- DROP TABLE public.goods_goods;

CREATE TABLE public.goods_goods
(
  id integer NOT NULL DEFAULT nextval('goods_goods_id_seq'::regclass),
  article_number bigint NOT NULL,
  title text NOT NULL,
  retail_price integer NOT NULL,
  weight_per_package integer NOT NULL,
  date_of_creation date NOT NULL,
  update_date date NOT NULL,
  category text NOT NULL,
  color text NOT NULL,
  stock text NOT NULL,
  price integer NOT NULL,
  CONSTRAINT goods_goods_pkey PRIMARY KEY (id),
  CONSTRAINT goods_goods_article_number_key UNIQUE (article_number)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.goods_goods
  OWNER TO postgres;
