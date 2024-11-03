output_json = {
  "version": "1.0",
  "truncation": None,
  "padding": None,
  "added_tokens": [
    {
      "id": 0,
      "content": "<bos>",
      "single_word": False,
      "lstrip": False,
      "rstrip": False,
      "normalized": False,
      "special": True
    },
    {
      "id": 1,
      "content": "<cls>",
      "single_word": False,
      "lstrip": False,
      "rstrip": False,
      "normalized": False,
      "special": True
    },
    {
      "id": 2,
      "content": "<pad>",
      "single_word": False,
      "lstrip": False,
      "rstrip": False,
      "normalized": False,
      "special": True
    },
    {
      "id": 3,
      "content": "<sep>",
      "single_word": False,
      "lstrip": False,
      "rstrip": False,
      "normalized": False,
      "special": True
    },
    {
      "id": 4,
      "content": "<eos>",
      "single_word": False,
      "lstrip": False,
      "rstrip": False,
      "normalized": False,
      "special": True
    },
    {
      "id": 5,
      "content": "<unk>",
      "single_word": False,
      "lstrip": False,
      "rstrip": False,
      "normalized": False,
      "special": True
    },
    {
      "id": 6,
      "content": "<mask>",
      "single_word": False,
      "lstrip": True,
      "rstrip": False,
      "normalized": False,
      "special": True
    }
  ],
  "normalizer": None,
  "pre_tokenizer": {
    "type": "WhitespaceSplit"
  },
  "post_processor": {
    "type": "TemplateProcessing",
    "single": [
      {
        "SpecialToken": {
          "id": "<bos>",
          "type_id": 0
        }
      },
      {
        "Sequence": {
          "id": "A",
          "type_id": 0
        }
      },
      {
        "SpecialToken": {
          "id": "<eos>",
          "type_id": 0
        }
      }
    ],
    "pair": [
      {
        "Sequence": {
          "id": "A",
          "type_id": 0
        }
      },
      {
        "Sequence": {
          "id": "B",
          "type_id": 1
        }
      }
    ],
    "special_tokens": {
      "<bos>": {
        "id": "<bos>",
        "ids": [
          0
        ],
        "tokens": [
          "<bos>"
        ]
      },
      "<eos>": {
        "id": "<eos>",
        "ids": [
          4
        ],
        "tokens": [
          "<eos>"
        ]
      }
    }
  },
  "decoder": {
    "type": "WordPiece",
    "prefix": "##",
    "cleanup": True
  },
  "model": {
    "type": "WordPiece",
    "unk_token": "<unk>",
    "continuing_subword_prefix": "##",
    "max_input_chars_per_word": 100,
    "vocab": {
      "<bos>": 0,
      "<cls>": 1,
      "<pad>": 2,
      "<sep>": 3,
      "<eos>": 4,
      "<unk>": 5,
      "<mask>": 6,
      # "#": 7,
    }
  }
}


elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',\
            'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',\
            'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co',\
            'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',\
            'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh',\
            'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',\
            'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu',\
            'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf',\
            'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl',\
            'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',\
            'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es',\
            'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs',\
            'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts',\
            'Og']