import { Component, OnInit } from '@angular/core';
import { Category } from '@app/shared/interfaces/category.interface';
import { CategoryService } from '@app/shared/services/category.service';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.scss']
})
export class CategoryComponent implements OnInit {

  categories: Category[] = [];
  constructor(private categorySvc: CategoryService) { }

  ngOnInit(): void {
    this.getDataFromService()
  }
  private getDataFromService(): void {
      this.categorySvc.getCategories().subscribe((res:any) => {
        const results = res;
        this.categories = results
      });
    }
}
