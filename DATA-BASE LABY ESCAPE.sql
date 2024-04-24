CREATE TABLE scores (score INT, pseudo VARCHAR(50), difficulty VARCHAR(50));

CREATE TABLE sauvegarde (id INT PRIMARY KEY AUTO_INCREMENT, pseudo
VARCHAR(50), score INT, difficulty VARCHAR(50), etat_matrice TEXT, entree_y
INT, entree_x INT, monstre_x INT, monstre_y INT, tp_x INT, tp_y INT, tp2_x
INT, tp2_y INT, tp3_x INT, tp3_y INT, tp4_x INT, tp4_y INT, tp5_x INT, tp5_y INT,
tp6_x INT, tp6_y INT, sortie_x INT, sortie_y INT, hauteur INT, largeur INT,
thesee_y INT, thesee_x INT);