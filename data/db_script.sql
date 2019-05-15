DROP TABLE IF EXISTS follower;
DROP TABLE IF EXISTS tweet;

--
-- Base de données :  `marketing_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `follower`
--

CREATE TABLE follower(
  `id_follower` VARCHAR(255) primary key,
  `name` VARCHAR(255),
  `screen_name` VARCHAR(255)
);

--
-- Déchargement des données de la table `Etudiant`
--

-- INSERT INTO....

CREATE TABLE tweet(
  `id_tweet` VARCHAR(255) primary key,
  `id_follower` VARCHAR(255),
  `date` timestamp NULL DEFAULT NULL,
  FOREIGN KEY (`id_follower`) REFERENCES follower(`id_follower`)
);

--
-- Déchargement des données de la table `Etudiant`
--

-- INSERT INTO....
