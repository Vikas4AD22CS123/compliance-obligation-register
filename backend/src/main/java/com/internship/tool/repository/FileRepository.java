package com.internship.tool.repository;

import com.internship.tool.entity.FileDocument;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FileRepository extends JpaRepository<FileDocument, Long> {
}