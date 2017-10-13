---
layout: post
---

```
        Properties properties = new Properties();
        File file = new File("/tmp/arquivo.properties"); FileInputStream fileInputStream = new FileInputStream(file); properties.load(fileInputStream); fileInputStream.close();
        for (String key : properties.stringPropertyNames()) {
            def value = properties.getProperty(key);
            param.put(key, value);
        }
```
fonte: 
https://stackoverflow.com/a/16342753
