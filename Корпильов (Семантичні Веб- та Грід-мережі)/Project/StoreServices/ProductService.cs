using Microsoft.EntityFrameworkCore;
using StoreData;
using StoreData.Models;
using System;
using System.Collections.Generic;
using System.Linq;

namespace StoreServices
{
    public class ProductService : IProduct
    {
        private StoreContext _context;
        public ProductService(StoreContext context)
        {
            _context = context;
        }
        public void Add(Product product)
        {
            _context.Add(product);
            _context.SaveChanges();
        }

        public IEnumerable<Product> GetAll()
        {
            return _context.Products
                .Include(product => product.Images);
        }

        public Product GetById(int id)
        {
            return GetAll()
                .FirstOrDefault(product => product.Id == id);
        }

        public Product GetByType(string type)
        {
            return GetAll()
                .FirstOrDefault(product => product.Type == type);
        }

        public IEnumerable<Image> GetImage(int id)
        {
            return GetById(id).Images;
        }

        public void Remove(Product product)
        {
            throw new NotImplementedException();
        }
    }
}
