using System;
using System.Collections.Generic;
using System.Text;

namespace StoreData.Models
{
    public class Image
    {
        public int Id { get; set; }
        public Product Product { get; set; }
        public string Url { get; set; }
        public string AltText { get; set; }
    }
}
