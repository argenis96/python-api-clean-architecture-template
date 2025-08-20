CREATE TABLE public.animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL CHECK (category IN (
        'Mamífero',
        'Ave',
        'Reptil',
        'Anfibio',
        'Insecto',
        'Pez'
    ))
);

INSERT INTO public.animals (id, name, category) VALUES
(1, 'León', 'Mamífero'),
(2, 'Tigre', 'Mamífero'),
(3, 'Elefante', 'Mamífero'),
(4, 'Águila', 'Ave'),
(5, 'Colibrí', 'Ave'),
(6, 'Tiburón Blanco', 'Pez'),
(7, 'Delfín', 'Mamífero'),
(8, 'Iguana', 'Reptil'),
(9, 'Cocodrilo', 'Reptil'),
(10, 'Mariposa Monarca', 'Insecto'),
(11, 'Pingüino', 'Ave'),
(12, 'Orca', 'Mamífero'),
(13, 'Caballo', 'Mamífero'),
(14, 'Camello', 'Mamífero'),
(15, 'Rana', 'Anfibio');