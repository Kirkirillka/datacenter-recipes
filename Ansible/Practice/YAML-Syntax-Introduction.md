# Синтаксис YAML

YAML - (акроним  "Yet Another Markup Language" - "Еще один язык разметки" ) - формат сериализации данных, концептуально близкий к языкам разметки, но ориентирован на удобочитаемость людьми.

YAML старается быть ближе к реальных структурам данных, существующих в языках программирования. YAML-файлы широко используется для описания конфигурации.


В качестве отступов используются пробелы (не табуляция)

Для первичного погружения как описывать файлы Ansible в формате YAML, нам потребуется:

- Для проверки того, как интерпретируется YAML, можно воспользоваться [сервисом](https://yaml-online-parser.appspot.com/)


### Определяем список элементов

```YAML
- Apple  
- Orange  
- Strawberry  
- Mango  
```

### Встраиваем список в одну строчку

```YAML
[Apple , Orange, Strawberry, Mango ]
```

```YAML
- [Apple , Orange, Strawberry, Mango ]
- [Egg, Cat]
```

### Определяем словарь ключ-значение

```YAML
version: 3.14
client: Kazan
```

### Встраиваем словарь в одну строчку

```YAML
{version: 3.14, client: Kazan}
```

### Определяем вложенный список

```YAML
- first root
  - one leaf
  - two leaf
- second root
  - lalala
```

### Определяем список со словарями

```YAML
- type: dictionary
  order: first
- type: dictionary
  order: second
```


### Совмещаем все вместе

```YAML
# Employee records
-  martin:
    name: Martin D'vloper
    job: Developer
    skills:
      - python
      - perl
      - pascal
-  tabitha:
    name: Tabitha Bitumen
    job: Developer
    skills:
      - lisp
      - fortran
      - erlang
```

Есть список с 2 элементами. Каждый элемент является словарем. Каждый из словарей содержит подсловарь, доступный по ключам martin, tabitha. Каждый из подсловарей содержит 3 поля, 2 из которых представляют собой символьную строку, а 3-е является списком
