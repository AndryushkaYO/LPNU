using StoreData.Models;
using System;
using System.Collections.Generic;
using System.Text;

namespace StoreData
{
    public interface IProduct
    {
        IEnumerable<Product> GetAll();
        Product GetById(int id);
        Product GetByType(string type);
        IEnumerable<Image> GetImage(int id);
        void Add(Product product);
        void Remove(Product product);
    }
}
